#
# PySNMP MIB module CISCO-IF-LINK-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IF-LINK-CONFIG-MIB
# Source digest sha256:b8504ddc340ac8f1a4e26cc1f6f9feb24622c6725dfedf536b84c5b53eb8a03e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoLocationSpecifier, = mibBuilder.importSymbols("CISCO-TC", "CiscoLocationSpecifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoIfLinkConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 175))
ciscoIfLinkConfigMIB.setRevisions(('2001-10-05 00:00', '2000-09-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setRevisionsDescriptions(('Add object cilTargetModuleFramingType in cilConfTable table', 'Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setLastUpdated('2001-10-05 00:00')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setContactInfo('Cisco Systems\n                     Customer Service\n                Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n                    Tel: +1 800 553-NETS\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setDescription('The MIB module for configuration of bulk distribution\n         (de-multiplexing of traffic from higher-bandwidth to \n         lower-bandwidth interfaces).\n\n         Terminology :\n\n         bulk-distribution        : The bulk distribution is the \n                                    feature by which a line/interface\n                                    on one module can replace the line\n                                    for the other.\n\n         bulk-distribution module : The module which links its \n                                    interfaces to the target module.\n\n         target module            : A module that gets incoming traffic\n                                    from a bulk distribution module \n                                    rather than from a back card.\n                      \n         The Module which supports bulk distribution, converts \n         traffic from its lines (may be T3, OC-N) to lines on \n         the target module (may be\n         T3, T1 etc). The bulk distribution is achieved by having a \n         point-to-point connection (bulk-distribution bus) between the \n         bulk-distribution module and the target module. The benefit \n         of bulk distribution is that the target module need not have\n         the back cards. The lines/interfaces from bulk-distribution\n         module will be used as lines for the target module.\n\n         An example is given here on linking interfaces.\n\n\n            |------------------------------------------------|\n            |                                                |\n            |             |------------------------------|   |\n            |             |           |             |    |   |\n            |             |           |-------------|    |   |\n          Ta|rget Module  |           |             |    |   |\n         -------       -------     -------     ---------------\n         |     |       |     |     |     |     |              |\n         |     |       |     |     |     |     |              |\n         |  T1 |       | T1  |     |T1   |     | Bulk         |\n         |card |       |card |     |card |     | Distribution |\n         |     |       |     |     |     |     |              |\n         |     |       |     |     |     |     | Module       |\n         |     |       |     |     |     |     |              |\n         |     |       |     |     |     |     | (T3 card)    |\n         |     |       |     |     |     |     |              |\n         -------       -------     -------      ---------------\n         ')
cilConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1))
cilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1))
cilConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cilConfTable.setStatus('current')
if mibBuilder.loadTexts: cilConfTable.setDescription('The interface link configuration table.')
cilConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IF-LINK-CONFIG-MIB", "cilSourceInterface"))
if mibBuilder.loadTexts: cilConfEntry.setStatus('current')
if mibBuilder.loadTexts: cilConfEntry.setDescription('An entry in the cilConfTable. This entry is used for  \n         linking an interface identified by cilSourceInterface\n         to an interface identified by cilTaregetModuleInterface.\n         The entries are created and deleted using the \n         cilRowStatus object. An interface on the bulk-distribution\n         module cannot be linked to multiple interfaces in the\n         target module.')
cilSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cilSourceInterface.setStatus('current')
if mibBuilder.loadTexts: cilSourceInterface.setDescription('An interface of the bulk-distribution module (Source) which\n         will be linked with the interface of the target module. It\n         represents an entry in the ifTable.')
cilTargetModuleInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 2), CiscoLocationSpecifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleInterface.setStatus('current')
if mibBuilder.loadTexts: cilTargetModuleInterface.setDescription('Location of the managed entity on the target module.\n         Following is the supported  format for this object and\n         all the values must be present.\n    \n         shelf=<value>, slot=<value>, subSlot=<value> port =<value>.\n\n         The zero length value for this object is not supported.')
cilRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilRowStatus.setStatus('current')
if mibBuilder.loadTexts: cilRowStatus.setDescription('This object is used to create a new row or modify or delete\n         an existing row in the table. The cilTargetModuleFramingType\n         need not be specified to create a row. If cilTargetModuleFramingType\n         is not specified, a default value will be assumed as described in the\n         description of cilTargetModuleFramingType.')
cilTargetModuleFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("dsx1D4", 2), ("dsx1ESF", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleFramingType.setStatus('current')
if mibBuilder.loadTexts: cilTargetModuleFramingType.setDescription('This object identifies the framing type of the target interface.\n         notApplicable(1) can not be set.\n\n             dsx1ESF         Extended SuperFrame DS1 (T1.107)\n             dsx1D4          AT&T D4 format DS1 (T1.107)\n\n         Default value is dsx1ESF(3) if cilTargetModuleInterface is a T1 interface \n         and sonet/sdh byte-synchronous mapping is used on the cilSourceInterface.\n         Otherwise, the default value is notApplicable(1).\n        ')
cilConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3))
cilConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1))
cilConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2))
cilConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBCompliance = cilConfigMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cilConfigMIBCompliance.setDescription('The Compliance statement for interface link configuration group.\n       This has been replaced by the cilConfigMIBComplianceRev1 statement.')
cilConfigMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBComplianceRev1 = cilConfigMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: cilConfigMIBComplianceRev1.setDescription('The Compliance statement for interface link configuration group.\n        This statement replaces cilConfigMIBCompliance statement.')
cilConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroup = cilConfMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cilConfMIBGroup.setDescription('These are objects related to interface link \n         configuration group. This group has been replaced\n         by cilConfMIBGroupRev1.')
cilConfMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"), ("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleFramingType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroupRev1 = cilConfMIBGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cilConfMIBGroupRev1.setDescription('These are objects related to interface link\n         configuration group. This group replaces the\n         cilConfMIBGroup.')
mibBuilder.exportSymbols("CISCO-IF-LINK-CONFIG-MIB", PYSNMP_MODULE_ID=ciscoIfLinkConfigMIB, cilConfEntry=cilConfEntry, cilConfMIBGroup=cilConfMIBGroup, cilConfMIBGroupRev1=cilConfMIBGroupRev1, cilConfTable=cilConfTable, cilConfig=cilConfig, cilConfigMIBCompliance=cilConfigMIBCompliance, cilConfigMIBComplianceRev1=cilConfigMIBComplianceRev1, cilConfigMIBCompliances=cilConfigMIBCompliances, cilConfigMIBConformance=cilConfigMIBConformance, cilConfigMIBGroups=cilConfigMIBGroups, cilConfigMIBObjects=cilConfigMIBObjects, cilRowStatus=cilRowStatus, cilSourceInterface=cilSourceInterface, cilTargetModuleFramingType=cilTargetModuleFramingType, cilTargetModuleInterface=cilTargetModuleInterface, ciscoIfLinkConfigMIB=ciscoIfLinkConfigMIB)
