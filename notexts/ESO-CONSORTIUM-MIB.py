#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 16:15:41 2022
# On host fv-az377-45 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Unsigned32, MibIdentifier, ModuleIdentity, Bits, snmpModules, Integer32, Counter32, Gauge32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "snmpModules", "Integer32", "Counter32", "Gauge32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "AutonomousType")
esoConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
esoConsortiumMIB.setRevisions(('2004-06-23 00:00', '2003-02-03 00:00', '2003-02-03 00:00',))
if mibBuilder.loadTexts: esoConsortiumMIB.setLastUpdated('200406230000Z')
if mibBuilder.loadTexts: esoConsortiumMIB.setOrganization('ESO (Extended Security Options) Consortium')
esoConsortiumMIBObjectIdentities = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
usmAESCfb128PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 2))
if mibBuilder.loadTexts: usmAESCfb128PrivProtocol.setStatus('deprecated')
usmAESCfb192PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 3))
if mibBuilder.loadTexts: usmAESCfb192PrivProtocol.setStatus('current')
usmAESCfb256PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 4))
if mibBuilder.loadTexts: usmAESCfb256PrivProtocol.setStatus('current')
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", PYSNMP_MODULE_ID=esoConsortiumMIB, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, usm3DESPrivProtocol=usm3DESPrivProtocol, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, esoConsortiumMIB=esoConsortiumMIB, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities)
