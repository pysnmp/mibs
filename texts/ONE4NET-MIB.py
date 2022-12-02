#
# PySNMP MIB module ONE4NET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/ONE4NET-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:10:33 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, MibIdentifier, iso, ObjectIdentity, NotificationType, Bits, TimeTicks, IpAddress, Counter64, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "NotificationType", "Bits", "TimeTicks", "IpAddress", "Counter64", "enterprises", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
one4net = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196))
one4net.setRevisions(('2002-01-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: one4net.setRevisionsDescriptions(('initial version',))
if mibBuilder.loadTexts: one4net.setLastUpdated('200201120000Z')
if mibBuilder.loadTexts: one4net.setOrganization('One4net GmbH')
if mibBuilder.loadTexts: one4net.setContactInfo('email:      support@one4net.com')
if mibBuilder.loadTexts: one4net.setDescription('one4net MIB.')
mibBuilder.exportSymbols("ONE4NET-MIB", one4net=one4net, PYSNMP_MODULE_ID=one4net)
