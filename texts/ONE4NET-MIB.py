#
# PySNMP MIB module ONE4NET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/ONE4NET-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:39:22 2024
# On host fv-az1766-730 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, NotificationType, Counter32, MibIdentifier, iso, enterprises, ObjectIdentity, Counter64, Unsigned32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "NotificationType", "Counter32", "MibIdentifier", "iso", "enterprises", "ObjectIdentity", "Counter64", "Unsigned32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
one4net = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196))
one4net.setRevisions(('2002-01-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: one4net.setRevisionsDescriptions(('initial version',))
if mibBuilder.loadTexts: one4net.setLastUpdated('200201120000Z')
if mibBuilder.loadTexts: one4net.setOrganization('One4net GmbH')
if mibBuilder.loadTexts: one4net.setContactInfo('email:      support@one4net.com')
if mibBuilder.loadTexts: one4net.setDescription('one4net MIB.')
mibBuilder.exportSymbols("ONE4NET-MIB", one4net=one4net, PYSNMP_MODULE_ID=one4net)
