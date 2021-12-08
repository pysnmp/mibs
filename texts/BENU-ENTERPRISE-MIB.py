#
# PySNMP MIB module BENU-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-ENTERPRISE-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:09:04 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Gauge32, iso, MibIdentifier, Bits, Unsigned32, enterprises, Integer32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Gauge32", "iso", "MibIdentifier", "Bits", "Unsigned32", "enterprises", "Integer32", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benu = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406))
benu.setRevisions(('2012-10-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benu.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: benu.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benu.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benu.setContactInfo('Benu Networks,Inc\n                          Corporate Headquarters\n                          300 Concord Road, Suite 110\n                          Billerica, MA 01821 USA\n                          Tel: +1 978-223-4700\n                          Fax: +1 978-362-1908\n                          Email: info@benunets.com')
if mibBuilder.loadTexts: benu.setDescription('The Structure of Management Information for the\n\t\t                 Benu Networks enterprise.')
mibBuilder.exportSymbols("BENU-ENTERPRISE-MIB", PYSNMP_MODULE_ID=benu, benu=benu)
