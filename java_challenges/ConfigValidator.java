import java.lang.annotation.*;
import java.util.List;

/**
 * Challenge 08 — Config Validator with Custom Annotations
 * ---------------------------------------------------------
 * Implement a reflection-based validator that checks annotated fields on any
 * plain Java object.
 *
 * <p>Define these field-level annotations (all {@code @Retention(RUNTIME)},
 * {@code @Target(FIELD)}):
 * <ul>
 *   <li>{@code @Required}         — field must not be null</li>
 *   <li>{@code @NotEmpty}         — String field must not be null or blank</li>
 *   <li>{@code @Range(min, max)}  — Number field must satisfy min &le; value &le; max</li>
 *   <li>{@code @Pattern(regex)}   — String field must fully match the regex</li>
 * </ul>
 *
 * <p>Validator API:
 * <pre>
 *   List&lt;Violation&gt; validate(Object obj)
 * </pre>
 *
 * <p>Violation record:
 * <pre>
 *   record Violation(String fieldName, String message) {}
 * </pre>
 *
 * <p>Rules:
 * <ul>
 *   <li>Inspect all declared fields including private ones (use {@code setAccessible}).</li>
 *   <li>Collect ALL violations, not just the first.</li>
 *   <li>Violations are returned in field declaration order.</li>
 *   <li>Unannotated fields are not checked.</li>
 * </ul>
 *
 * <p>Example usage:
 * <pre>
 *   class ServiceConfig {
 *       {@literal @}NotEmpty  String name;
 *       {@literal @}Range(min = 1, max = 100) int replicas;
 *       {@literal @}Pattern("[a-z0-9/:.]+") String image;
 *   }
 *   var violations = new ConfigValidator().validate(new ServiceConfig());
 * </pre>
 */
public class ConfigValidator {

    // -------------------------------------------------------------------------
    // Annotations
    // -------------------------------------------------------------------------

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.FIELD)
    public @interface Required {}

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.FIELD)
    public @interface NotEmpty {}

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.FIELD)
    public @interface Range {
        double min() default Double.NEGATIVE_INFINITY;
        double max() default Double.POSITIVE_INFINITY;
    }

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.FIELD)
    public @interface Pattern {
        String regex();
    }

    // -------------------------------------------------------------------------
    // Violation record
    // -------------------------------------------------------------------------

    public record Violation(String fieldName, String message) {}

    // -------------------------------------------------------------------------
    // Validator
    // -------------------------------------------------------------------------

    public List<Violation> validate(Object obj) {
        throw new UnsupportedOperationException("not implemented");
    }
}
