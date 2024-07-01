#
# PySNMP MIB module EdgeSwitch-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-REF-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 10:53:29 2024
# On host fv-az665-510 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, MibIdentifier, Integer32, Unsigned32, Counter32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, enterprises, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "MibIdentifier", "Integer32", "Unsigned32", "Counter32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "enterprises", "ObjectIdentity", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Broadcom Inc')
broadcomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1))
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("EdgeSwitch-REF-MIB", fastPath=fastPath, broadcom=broadcom, AgentPortMask=AgentPortMask, PYSNMP_MODULE_ID=broadcom, broadcomProducts=broadcomProducts)
